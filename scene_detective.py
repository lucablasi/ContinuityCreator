def scene_detective(filepath, start_time=00.000, duration='max',
                    threshold=30.0, min_scene_len=15):
    """
    Performs scene detection on specified file.
    Output is sc_list

    :param filepath: video file to be processed
    :param start_time: start time [sec] of processing
    :param duration: duration [sec] from start time to be processed
    :param threshold: ContentDetector scene change threshold
    :param min_scene_len: ContentDetector minimum scene length

    :type filepath: basestring
    :type start_time: float
    :type duration: float
    :type threshold: float
    :type min_scene_len: float
    """
    import os

    from scenedetect.detectors import ContentDetector
    from scenedetect.scene_manager import SceneManager
    from scenedetect.stats_manager import StatsManager
    from scenedetect.video_manager import VideoManager

    stats_file_path = filepath + '.stats.csv'

    # Create a video_manager point to video file. Note that multiple
    # videos can be appended by simply specifying more file paths in the list
    # passed to the VideoManager constructor. Note that appending multiple videos
    # requires that they all have the same frame size, and optionally, framerate.
    video_manager = VideoManager([filepath])
    stats_manager = StatsManager()
    scene_manager = SceneManager(stats_manager)
    # Add ContentDetector algorithm (constructor takes detector options like threshold).
    scene_manager.add_detector(ContentDetector(threshold=threshold, min_scene_len=min_scene_len))
    base_timecode = video_manager.get_base_timecode()

    try:
        # If stats file exists, load it.
        if os.path.exists(stats_file_path):
            # Read stats from CSV file opened in read mode:
            with open(stats_file_path, 'r') as stats_file:
                stats_manager.load_from_csv(stats_file, base_timecode)

        start_time = base_timecode + float(start_time)
        if duration != 'max':
            end_time = start_time + float(duration)
            video_manager.set_duration(start_time=start_time, end_time=end_time)
        video_manager.set_duration(start_time=start_time)

        # Set downscale factor to improve processing speed.
        video_manager.set_downscale_factor()

        # Start video_manager.
        video_manager.start()

        # Perform scene detection on video_manager.
        scene_manager.detect_scenes(frame_source=video_manager)

        # Obtain list of detected scenes.
        sc_list = scene_manager.get_scene_list(base_timecode)
        # Like FrameTimecodes, each scene in the sc_list can be sorted if the
        # list of scenes becomes unsorted.

        # We only write to the stats file if a save is required:
        if stats_manager.is_save_required():
            with open(stats_file_path, 'w') as stats_file:
                stats_manager.save_to_csv(stats_file, base_timecode)

    finally:
        video_manager.release()

    return sc_list
