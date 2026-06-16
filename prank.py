import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image

import cv2
import mediapipe as mp

class GestureApp(App):
    def build(self):
        # تصميم واجهة التطبيق
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.title_label = Label(
            text="تطبيق التحكم بالإيماءات - جاري تشغيل الكاميرا", 
            font_size='20sp', 
            size_hint_y=0.1
        )
        self.layout.add(self.title_label)
        
        # مكان عرض كاميرا الموبايل جوه الأبلكيشن
        self.image_widget = Image(size_hint_y=0.8)
        self.layout.add(self.image_widget)
        
        # زرار للخروج
        self.exit_button = Button(text="إغلاق التطبيق", size_hint_y=0.1)
        self.exit_button.bind(on_press=self.stop)
        self.layout.add(self.exit_button)
        
        # تجهيز مكتبة الذكاء الاصطناعي لـ الإيد
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        
        # فتح كاميرا الموبايل الخلفية أو الأمامية
        self.capture = cv2.VideoCapture(0)
        
        # تشغيل الكود وتحديث الشاشة باستمرار (30 فريم في الثانية)
        Clock.schedule_interval(self.update, 1.0 / 30.0)
        
        return self.layout

    def update(self, dt):
        # قراءة الفريم من الكاميرا
        ret, frame = self.capture.read()
        if not ret:
            return

        # عزل الألوان عشان MediaPipe يفهمها (بايثون بيقرا BGR وإحنا عايزينه RGB)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        # لو الذكاء الاصطناعي لقط إيد في الكاميرا
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # رسم النقط الخضراء على الصوابع في الشاشة
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                
                # هنا بنجيب نقطة صباع السبابة (index finger) كمثال عشان نحدد مكانه
                index_finger = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
                
                # اختبار بسيط: لو رفعت صباعك فوق نص الشاشة، التطبيق هيحس بيك
                if index_finger.y < 0.4:
                    self.title_label.text = "تم رصد حركة للأعلى! (تقليب)"
                else:
                    self.title_label.text = "يتم الآن تتبع حركة يدك..."

        # تحويل صورة OpenCV لشكل ينفع يتعرض جوه واجهة الـ Kivy
        buffer = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image_widget.texture = texture

    def on_stop(self):
        # قفل الكاميرا أول ما التطبيق يقفل عشان متهنجش الموبايل
        self.capture.release()

if __name__ == '__main__':
    GestureApp().run()