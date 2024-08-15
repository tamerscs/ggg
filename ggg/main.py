from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
import arabic_reshaper
from bidi.algorithm import get_display
from kivy.core.window import Window

def reverse_arabic_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        # صورة الخلفية
        background_image = Image(source='C:/Users/emada/Desktop/ggg/logo.jpg', allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        background_image.color = (1, 1, 1, 0.4)  # زيادة الشفافية
        layout.add_widget(background_image)

        # زر "أصنافنا"
        items_button = Button(
            text=reverse_arabic_text('أصنافنا'),
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.75},
            font_name='Amiri-Regular',
            font_size=24,
            background_color=(1, 0, 0, 0.5),  # خلفية الزر أحمر مع شفافية 0.5
            color=(1, 1, 1, 1)  # لون الخط أبيض
        )
        items_button.bind(on_press=self.change_screen)
        layout.add_widget(items_button)

        # زر "موقعنا وافرعنا"
        branches_button = Button(
            text=reverse_arabic_text('موقعنا وافرعنا'),
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            font_name='Amiri-Regular',
            font_size=24,
            background_color=(1, 0, 0, 0.5),  # خلفية الزر أحمر مع شفافية 0.5
            color=(1, 1, 1, 1)  # لون الخط أبيض
        )
        branches_button.bind(on_press=self.change_screen)
        layout.add_widget(branches_button)

        # زر "من نحن"
        about_us_button = Button(
            text=reverse_arabic_text('من نحن'),
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            font_name='Amiri-Regular',
            font_size=24,
            background_color=(1, 0, 0, 0.5),  # خلفية الزر أحمر مع شفافية 0.5
            color=(1, 1, 1, 1)  # لون الخط أبيض
        )
        about_us_button.bind(on_press=self.change_screen)
        layout.add_widget(about_us_button)

        # زر "تواصل معنا"
        contact_button = Button(
            text=reverse_arabic_text('تواصل معنا'),
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            font_name='Amiri-Regular',
            font_size=24,
            background_color=(1, 0, 0, 0.5),  # خلفية الزر أحمر مع شفافية 0.5
            color=(1, 1, 1, 1)  # لون الخط أبيض
        )
        contact_button.bind(on_press=self.change_screen)
        layout.add_widget(contact_button)

        # زر الخروج
        exit_button = Button(
            text=reverse_arabic_text('خروج'),
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.15},
            font_name='Amiri-Regular',
            font_size=24,
            background_color=(1, 1, 1, 0.5),  # خلفية الزر أبيض مع شفافية 0.5
            color=(1, 1, 1, 1)  # لون الخط أسود
        )
        exit_button.bind(on_press=self.exit_app)
        layout.add_widget(exit_button)

        self.add_widget(layout)

    def change_screen(self, instance):
        if instance.text == reverse_arabic_text('أصنافنا'):
            self.manager.current = 'items_screen'
        elif instance.text == reverse_arabic_text('موقعنا وافرعنا'):
            self.manager.current = 'branches_screen'
        elif instance.text == reverse_arabic_text('من نحن'):
            self.manager.current = 'about_us_screen'
        elif instance.text == reverse_arabic_text('تواصل معنا'):
            self.manager.current = 'contact_screen'

    def exit_app(self, instance):
        App.get_running_app().stop()

class ItemsScreen(Screen):
    def __init__(self, **kwargs):
        super(ItemsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # ScrollView for horizontal scrolling
        scrollview = ScrollView(
            do_scroll_x=True,
            do_scroll_y=False,
            size_hint=(1, 0.9)
        )
        scrollview_layout = BoxLayout(orientation='horizontal', size_hint_x=None, width=Window.width * 2, spacing=5)
        
        items = [
            {"path": "C:/Users/emada/Desktop/ggg/01.png", "description": "مطعم عماد الدين"},
            {"path": "C:/Users/emada/Desktop/ggg/03.png", "description": "  اصناف متنوعة"},
            {"path": "C:/Users/emada/Desktop/ggg/13.jpg", "description": "  وجبات شرقية "},
            {"path": "C:/Users/emada/Desktop/ggg/14.jpg", "description": "  كبب متنوعة"},
            {"path": "C:/Users/emada/Desktop/ggg/17.jpg", "description": "   دجاج محشي"},
            {"path": "C:/Users/emada/Desktop/ggg/18.png", "description": "  لحم بالعجين"},
            {"path": "C:/Users/emada/Desktop/ggg/7.jpg", "description": "  بيتزا  بانواعها"},
            {"path": "C:/Users/emada/Desktop/ggg/16.jpg", "description": "  ورق عنب"},
           
            # أضف المزيد من الصور والأوصاف هنا
        ]
        
        for item in items:
            item_layout = BoxLayout(orientation='vertical', size_hint_x=None, width=200, padding=10, spacing=5)
            img = Image(source=item["path"], size_hint=(1, None), height=200)
            desc = Label(
                text=reverse_arabic_text(item["description"]),
                font_name='Amiri-Regular',
                font_size=20,
                color=(1, 1, 1, 1),  # لون الخط أبيض
                size_hint=(1, None),
                height=50
            )
            item_layout.add_widget(img)
            item_layout.add_widget(desc)
            scrollview_layout.add_widget(item_layout)

        scrollview.add_widget(scrollview_layout)
        layout.add_widget(scrollview)

        back_button = Button(
            text=reverse_arabic_text('العودة'),
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5},
            font_name='Amiri-Regular',
            font_size=24,
            background_color=(50, 0, 0, 0.5),  # خلفية الزر أحمر مع شفافية 0.5
            color=(1, 1, 1, 1)  # لون الخط أبيض
        )
        back_button.bind(on_press=self.back_to_main)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def back_to_main(self, instance):
        self.manager.current = 'main_screen'

class BranchesScreen(Screen):
    def __init__(self, **kwargs):
        super(BranchesScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        # صورة الخلفية مع زيادة الشفافية
        background_image = Image(source='C:/Users/emada/Desktop/ggg/33.png', allow_stretch=True, keep_ratio=False, size_hint=(1, 1), opacity=0.3)
        layout.add_widget(background_image)

        # ترتيب النصوص في BoxLayout عمودي مع زيادة المسافات
        branches_layout = BoxLayout(orientation='vertical', padding=[50, 50], spacing=100, size_hint=(0.8, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.6})

        branches_info = [
            {"name": "الفرع الرئيسي", "location": "\n\nادلب - سرمدا/ مفرق العامود"},
            {"name": "فرع حزانو", "location": "\n\nاتستراد ادلب - حزانو    مول الغيدق /طابق اول"},
            {"name": "فرع الباب", "location": "\n\nمدينة الباب / دوار الكف"},
        ]
        
        for branch in branches_info:
            branch_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)  # زيادة المسافات بين الأسطر
            name_label = Label(
                text=reverse_arabic_text(branch["name"]),
                font_name='Amiri-Regular',
                font_size=24,
                color=(1, 1, 1, 1)  # لون الخط أبيض
            )
            location_label = Label(
                text=reverse_arabic_text(branch["location"]),
                font_name='Amiri-Regular',
                font_size=20,
                color=(1, 1, 1, 1)  # لون الخط أبيض
            )
            branch_layout.add_widget(name_label)
            branch_layout.add_widget(location_label)
            branches_layout.add_widget(branch_layout)

        layout.add_widget(branches_layout)

        back_button = Button(
            text=reverse_arabic_text('العودة'),
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'y': 0.05},
            font_name='Amiri-Regular',
            font_size=24,
            background_color=(50, 0, 0, 0.5),  # خلفية الزر أحمر مع شفافية 0.5
            color=(1, 1, 1, 1)  # لون الخط أبيض
        )
        back_button.bind(on_press=self.back_to_main)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def back_to_main(self, instance):
        self.manager.current = 'main_screen'



class AboutUsScreen(Screen):
    def __init__(self, **kwargs):
        super(AboutUsScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        # صورة الخلفية
        background_image = Image(source='C:/Users/emada/Desktop/ggg/1.jpg', allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        background_image.color = (1, 1, 1, 0.5)  # زيادة الشفافية
        layout.add_widget(background_image)

        about_us_text = "  نحن سلسلة مطاعم عماد الدين بافرعنا الثلاثة        \nمختصون بالطعام الشرقي                  \n والوجبات الشرقية والمناسف                \n نتشرف بخدمة عملائنا الكرام               \n وفق اعلى المعايير والمواصفات              \nومستعدون لتلبية كافة الطلبات.              "

        about_us_label = Label(
            text=reverse_arabic_text(about_us_text),
            font_name='Amiri-Regular',
            font_size=20,
            color=(0, 1, 0, 1),  # لون الخط أبيض
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        layout.add_widget(about_us_label)

        back_button = Button(
            text=reverse_arabic_text('العودة'),
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            font_name='Amiri-Regular',
            font_size=24,
            background_color=(50, 0, 0, 0.5),  # خلفية الزر أحمر مع شفافية 0.5
            color=(1, 1, 1, 1)  # لون الخط أبيض
        )
        back_button.bind(on_press=self.back_to_main)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def back_to_main(self, instance):
        self.manager.current = 'main_screen'


class ContactScreen(Screen):
    def __init__(self, **kwargs):
        super(ContactScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        # صورة الخلفية
        background_image = Image(source='C:/Users/emada/Desktop/ggg/02.png', allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        background_image.color = (1, 1, 1, 0.3)  # زيادة الشفافية
        layout.add_widget(background_image)

        contact_info = " للتواصل معنا:             \n مطبخ ومندي عماد الدين -فرع سرمدا:\n     +352681130066        \n        مطعم عماد الدين حزانو :       \n     +352681116633        \n مطبخ ومندي عماد الدين - الباب:  \n +905386222056        \n "
        
        contact_label = Label(
            text=reverse_arabic_text(contact_info),
            font_name='Amiri-Regular',
            font_size=24,
            color=(1, 1, 1, 1),  # لون الخط أبيض
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        layout.add_widget(contact_label)

        back_button = Button(
            text=reverse_arabic_text('العودة'),
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            font_name='Amiri-Regular',
            font_size=24,
            background_color=(50, 0, 0, 0.5),  # خلفية الزر أحمر مع شفافية 0.5
            color=(1, 1, 1, 1)  # لون الخط أبيض
        )
        back_button.bind(on_press=self.back_to_main)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def back_to_main(self, instance):
        self.manager.current = 'main_screen'

class ArabicApp(App):
    def build(self):
        Window.size = (390, 470)
        Window.clearcolor = (0, 0, 0, 1)  # خلفية التطبيق أسود
        
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(ItemsScreen(name='items_screen'))
        sm.add_widget(BranchesScreen(name='branches_screen'))
        sm.add_widget(AboutUsScreen(name='about_us_screen'))
        sm.add_widget(ContactScreen(name='contact_screen'))

        return sm

if __name__ == '__main__':
    ArabicApp().run()
