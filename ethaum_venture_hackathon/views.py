from django.shortcuts import render
import pyrebase
from django.views import generic, View
from django.contrib import auth

config = {
    'apiKey': "AIzaSyDBtClJv-4mQyAT8WemilziLsqUx-JHvZM",
    'authDomain': "hackathonvceth.firebaseio.com",
    'databaseURL': "https://hackathonvceth.firebaseio.com",
    'projectId': "hackathonvceth",
    'storageBucket': "hackathonvceth.appspot.com",
    # 'messagingSenderId': "579985583952"
}
firebase = pyrebase.initialize_app(config)
authen = firebase.auth()
storage = firebase.storage()

def upload_file():
    path_cloud = "test/t1.txt"
    path_local = "files/t1.txt"
    storage.child(path_cloud).put(path_local)
    
def download_file():
    path_cloud = "fzLFnU9MjhaEzx249vhb0d3DVvg2/20200328_211446.mp4"
    path_local = "files/20200328_211446.mp4"
    storage.child(path_cloud).download(path_local)

# : if request.auth != null

class SignIn(View):
    template_name = 'signin.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        passw = request.POST.get("pass")
        try:
            user = authen.sign_in_with_email_and_password(email, passw)
        except:
            message = "invalid cerediantials"
            return render(request, self.template_name, {"msg": message})
        # print(user['idToken'])
        session_id=user['idToken']
        request.session['uid']=str(session_id)
        return render(request, "welcome.html", {"e": email})


class Logout(View):
    template_name = 'signin.html'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return render(request, self.template_name)

class TestView(View):
    template_name = 'welcome.html'

    def get(self, request, *args, **kwargs):
        upload_file()
        # download_file()
        return render(request, self.template_name)