import streamlit as st
from object_detection_image_video_streamlit import *
from PIL import Image
import tempfile

def main():

    st.title("Object Detection Using YoLo-NAS")
    st.sidebar.title("Settings")
    st.sidebar.subheader("Parameters")
    st.markdown(
        """
        <style>
        [data-testid="stSidebar][aria-expanded="true] > div:first-child{
        width: 300px;
        }
        [data-testid="stSidebar][aria-expanded="true] > div:first-child{
        width: 300px;
        margin-left:-300px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    app_mode = st.sidebar.selectbox('Choose the App Mode', ['About App', 'Run on Image', 'Run on Video'])
    if app_mode == "About App":
        st.markdown("In this project I am using **YOLO-NAS** to do object detection on images and videos. In addition to that, I am using **streamlit** as the graphical user interface")
        st.markdown(
        """
        <style>
        [data-testid="stSidebar][aria-expanded="true] > div:first-child{
        width: 300px;
        }
        [data-testid="stSidebar][aria-expanded="true] > div:first-child{
        width: 300px;
        margin-left:-300px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
        st.video("https://youtu.be/Q2S5tLcuVgM")
        st.markdown('''
                    # About Me
                    I am Dhruv, a masters student in AI. Kindly check the full video to see the results  
        ''')

    elif app_mode == "Run on Image":
        st.markdown("----")
        confidence = st.sidebar.slider('Confidence', min_value=0.0, max_value=1.0, value=0.35)
        st.sidebar.markdown("----")
        st.markdown(
        """
        <style>
        [data-testid="stSidebar][aria-expanded="true] > div:first-child{
        width: 300px;
        }
        [data-testid="stSidebar][aria-expanded="true] > div:first-child{
        width: 300px;
        margin-left:-300px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
        img_file_buffer = st.sidebar.file_uploader("Upload an image", type = ["jpg", "jpeg", "png"])
        DEMO_IMAGE = 'D:\MSAI Lectures and Documents\Advanced Computer Vision\Yolo-NAS\Image\image10.jpg'
        if img_file_buffer is not None:
            img = cv2.imdecode(np.fromstring(img_file_buffer.read(), np.uint8),1) 
            image = np.array(Image.open(img_file_buffer))
        else:
            img = cv2.imread(DEMO_IMAGE)
            image = np.array(Image.open(DEMO_IMAGE))
        st.sidebar.text("Original Image")
        st.sidebar.image(image)
        load_yolonas_process_each_image(image, confidence, st)

    elif app_mode == "Run on Video":
        st.markdown(
        """
        <style>
        [data-testid="stSidebar][aria-expanded="true] > div:first-child{
        width: 300px;
        }
        [data-testid="stSidebar][aria-expanded="true] > div:first-child{
        width: 300px;
        margin-left:-300px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
        st.sidebar.markdown('----')
        use_webcam = st.sidebar.checkbox('use Webcam')
        st.sidebar.markdown('-----')
        video_file_buffer = st.sidebar.file_uploader("Upload a video", type = ["mp4", "avi", "mov", "asf"])
        DEMO_VIDEO = 'D:\MSAI Lectures and Documents\Advanced Computer Vision\Yolo-NAS\Video\street_view.mp4'
        tffile = tempfile.NamedTemporaryFile(suffix = '.mp4', delete=False)
        if not video_file_buffer:
            if use_webcam:
                tffile.name = 0
            else:
                vid = cv2.VideoCapture(DEMO_VIDEO)
                tffile.name = DEMO_VIDEO
                demo_vid = open(tffile.name, 'rb')
                demo_bytes = demo_vid.read()
                st.sidebar.text('Input Video')
                st.sidebar.video(demo_bytes)
        else:
            tffile.write(video_file_buffer.read())
            demo_vid = open(tffile.name, 'rb')
            demo_bytes = demo_vid.read()
            st.sidebar.text('Input Video')
            st.sidebar.video(demo_bytes)
        stframe = st.empty()
        st.markdown("<hr/>", unsafe_allow_html = True)
        kpi1, kpi2, kpi3 = st.columns(3)
        with kpi1:
            st.markdown("**Frame rate**")
            kpi1_text = st.markdown("0")
        
        with kpi2:
            st.markdown("**Width**")
            kpi2_text = st.markdown("0")
        
        with kpi3:
            st.markdown("**Height**")
            kpi3_text = st.markdown("0")
        st.markdown("<hr/>", unsafe_allow_html=True)
        load_yolonas_process_each_frame(tffile.name, kpi1_text, kpi2_text, kpi3_text, stframe)

if __name__=='__main__':
    try:
        main()
    except SystemExit:
        pass
