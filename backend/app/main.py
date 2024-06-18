from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from backend.app.config import server_setting
from backend.app.api.routes import summarize_router


origins = [
    # Move origin to a variable, also include PORT setting in .env file, which can be handy
    f'http://localhost:{server_setting.PORT}'
]

app = FastAPI()

# adding middleware, can be used in future
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["*"],
)

# registrating summarize router
app.include_router(summarize_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=server_setting.PORT)