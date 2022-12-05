import fastapi
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from extras.palette import palette_random, palette_image, get_image

app = fastapi.FastAPI()
pages = Jinja2Templates(directory="templates")
app.add_middleware(CORSMiddleware, allow_origins=["*"])


class NoCacheFileResponse(fastapi.responses.FileResponse):
    def __init__(self, path: str, **kwargs):
        super().__init__(path, **kwargs)
        self.headers["Cache-Control"] = "no-cache"


@app.get("/", response_class=fastapi.responses.HTMLResponse)
async def install(request: fastapi.Request):
    return fastapi.responses.RedirectResponse(
        "https://alpha.deta.space/discovery/@sofa/pallets"
    )


@app.get("/demo", response_class=fastapi.responses.HTMLResponse)
async def demo(request: fastapi.Request):
    items = palette_random()
    return pages.TemplateResponse(
        "demo.html",
        {"request": request, "items": items},
    )


@app.get("/github", response_class=fastapi.responses.HTMLResponse)
async def github(request: fastapi.Request):
    return fastapi.responses.RedirectResponse(
        "https://github.com/SlumberDemon/Palettes"
    )


@app.get("/text/palette")
async def text_palette(text: str):
    data = palette_image(await get_image(text))
    while len(data) != 5:
        data.append("#000000")
    return {"colors": data}


@app.get("/random/palette")
async def random_palette():
    data = palette_random()
    return {"colors": data}


"""

@app.get("/image/palette")
async def image_palette(image: str):
    data = palette_image(image)
    while len(data) != 5:
        data.append("#000000")
    return {"colors": data}
"""

"""
@app.get("/complementary/palette")
async def complementary_palette(hex: str):
    data = palette_complementary(hex)
    return {"colors": data}
"""


@app.get("/static/{path:path}")
async def static(path: str):
    return NoCacheFileResponse(f"./static/{path}")
