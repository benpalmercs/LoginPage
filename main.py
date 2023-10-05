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
        self.ids.invalid_creds.text = " "

    def sign_in(self, username, password):
        if username in users and password == users[username]:
            self.manager.current = "welcome"
            self.ids.invalid_creds.text = " "
        else:
            self.ids.invalid_creds.text = "invalid credentials"
            self.ids.invalid_creds.color = "red"


class WelcomeScreen(Screen):
    def logout(self):
        self.manager.current = "signin"


def checknum(text, numbers):
    for i in numbers:
        if i in text:
            return True


def checkchar(text, characters):
    for i in characters:
        if i in text:
            return True


class RegisterScreen(Screen):
    def register_account(self, username, password, password2):
        if password == password2 and password != password.lower() and password != password.upper() and len(
                password) > 8 and username not in users and checknum(password, "1234567890") and checkchar(password,
                                                                                                           "`~!@#$%^&*()_-+=[]}{\|?/<>"):
            users.update({username: password})
            self.manager.current = "signin"
        else:
            self.ids.bad_account.text = "invalid username or password"
            self.ids.bad_account.color = "red"
    def quit(self):
        self.manager.current = "signin"


Builder.load_file("LoginProject.kv")
LoginProjectApp().run()
