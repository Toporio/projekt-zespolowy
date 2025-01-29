from microdot_asyncio import Microdot, Response
from microdot_utemplate import render_template

app = Microdot()
Response.default_content_type = 'text/html'

@app.route('/', methods=['GET', 'POST'])
async def index(request):
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
async def submit(request):
    form_data = await request.form.get('selected_item')
    print(form_data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
