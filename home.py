import streamlit as st
from PIL import Image


def home():

    header = st.container()
    explain = st.container()
    model = st.container()
    pre = st.container()

    with header:
        st.markdown(
            "<h1 style='text-align: center; color:Red ;'>REAL TIME HUMAN POSE ESTIMATION: </h1>", unsafe_allow_html=True)

    with explain:
        st.header("Human Pose Estimation :person_with_ball:")
        st.write("Human body pose estimation from images or video plays a central role in various applications such as health tracking, sign language recognition, and gestural control. This task is challenging due to a wide variety of poses, numerous degrees of freedom, and occlusions")
        st.write("Pose Estimation consists of three different blocks")
        st.write("1 Body+Foot detection")
        st.write("2 Hand detection")
        st.write("3 Face detection.")
        st.markdown("## Pose Estimation ##")
        st.write("Single-Person Pose Estimation: (MediaPipe BlazePose)")
        blaze = ['images/blazepose.gif',
                 'images/blazepose2.gif', 'images/blazepose3.gif']
        st.image(blaze, use_column_width=True * len(blaze))

    with model:
        st.markdown(
            "<h2 style='text-align: center; color:Red ;'>Human Pose Estimation </h2>", unsafe_allow_html=True)
        st.markdown("###  BLAZEPOSE : ### ")
        st.write("BlazePose, a lightweight convolutional neural network architecture for human pose estimation that is tailored for real-time inference on mobile devices.During inference, the network produces 33 body keypoints for a single person and runs at around 30 frames per second . This makes it particularly suited to real-time use cases like fitness tracking and sign language recognition.Our main contributions include a novel body pose tracking solution and a lightweight body pose estimation neural network that uses both heatmaps and regression to keypoint coordinates.")
        st.image("images/wall.gif")

    with pre:
        st.sidebar.markdown(
            "<h1 style='color:Red ;'>Requirements</h1>", unsafe_allow_html=True)
        st.sidebar.markdown("## [Python](https://www.python.org/downloads/)")
        st.sidebar.code('install python3 and greater')
        st.sidebar.markdown("## [Numpy](https://opencv.org/)")
        st.sidebar.code('$pip install opencv-python')
        st.sidebar.markdown("## [Pandas](https://pandas.pydata.org/)")
        st.sidebar.code('$pip install pandas')
        st.sidebar.markdown(
            "## [scikit-learn](https://scikit-learn.org/stable/)")
        st.sidebar.code('$pip install scikit-learn')
        st.sidebar.markdown("## [Matplotlib](https://matplotlib.org/)")
        st.sidebar.code('$pip install matplotlib')
        st.sidebar.markdown("## [OpenCV](https://opencv.org/)")
        st.sidebar.code('$pip install opencv-python')
        st.sidebar.markdown("## [Mediapipe](https://mediapipe.dev/)")
        st.sidebar.code('$pip install mediapipe')
        st.sidebar.markdown("## [streamlit](https://streamlit.io/)")
        st.sidebar.code('$pip install streamlit')
