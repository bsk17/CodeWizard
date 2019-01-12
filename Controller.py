# importing the web package
import web

# this is to create the URL
url = (
    '/', 'home', '/register', 'register'
)

# this is to instantiate the application
app = web.application(url, globals())

# the render will go to the directed folder to search for the template
# web is the package, template is the class, render is the method
render = web.template.render("Views/Templates", base="MainLayout")


# class definition
class home:
    def GET(self):
        return render.home()


class register:
    def GET(self):
        return render.Register()


# this is to run the app


if __name__ == "__main__":
    app.run()
