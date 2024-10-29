import web
import httpx  # Para realizar la solicitud HTTP a la API externa

# URLs de la aplicación
urls = (
    '/', 'Index',
)
render = web.template.render('templates')
app = web.application(urls, globals())

class Index:
    def GET(self):
        # Hacer la solicitud a la API para obtener los productos
        try:
            response = httpx.get("http://localhost:8081/api/productos")
            productos = response.json()
        except httpx.HTTPStatusError as e:
            print(f"Error al hacer la solicitud: {e}")
            productos = []

        # Pasar los productos a la plantilla index.html
        return render.index(productos)

if __name__ == "__main__":
    app.run()
