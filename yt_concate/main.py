from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCmahFSxXfkFbDdF425NwHJw'
def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        GetVideoList(),
        ]

    p = Pipeline(steps)
    p.run(inputs)

if __name__ == '__main__':
    main()