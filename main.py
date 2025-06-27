from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from routes import payment  # <- this is your PayMongo router

app = FastAPI(title="Payment Service")

# Include the payment router
app.include_router(payment.router, prefix='/payment', tags=['payment'])

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://bleu-oos.vercel.app",  # OOS frontend

        "https://bleu-ums.onrender.com",  # Auth service

        "https://ordering-service.onrender.com",  #ordering service
        "https://bleu-pos-eight.vercel.app", # pos frontend

    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Run the app (only used when running as a script directly)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=7005, host="127.0.0.1", reload=True)