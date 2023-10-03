# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen

# Builder.load_file("LoginPage.kv")
# class LoginPageApp(App):
# def build(self):
# return LoginManager()

# class LoginManager(ScreenManager):
# pass

# class Question1Screen(Screen):
# def answer_question(self,bool):
# if bool:
# self.manager.current = "correct"
# else:
# self.manager.current = "error"


# class Question2Screen(Screen):
# def answer_question(self,text):
# if text.lower() == "deep in the heart of texas":
# self.manager.current = "correct"
# else:
# self.ids.invalid_guess.text = "Invalid guess.\n Try again!"
# self.ids.invalid_guess.color = "red"
# class CorrectScreen(Screen):
# def advance(self):
# self.manager.current = "question2"

# class ErrorScreen(Screen):
# def advance(self):
# self.manager.current = "question2"


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

users = {"BP2007": "123!Codingrules", "B": "1"}


class LoginProjectApp(App):
    def build(self):
        return LoginManager()


class LoginManager(ScreenManager):
    pass


class SignInScreen(Screen):
    def register(self):
        self.manager.current = "register"
    def sign_in(self,username,password):
        if (username in users.items) and (users[username] == password):
            self.manager.current = "welcome"
        else:
            self.ids.invalid_creds.text = "invalid credentials"
            self.ids.invalid_creds.color = "red"



class WelcomeScreen(Screen):
    pass


class RegisterScreen(Screen):
    pass


Builder.load_file("LoginProject.kv")
LoginProjectApp().run()
