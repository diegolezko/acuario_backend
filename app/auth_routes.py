from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

# Import correctos
from . import database, models, auth, schemas

router = APIRouter(prefix="/auth", tags=["Auth"])


# =========================
#  LOGIN
# =========================
@router.post("/login", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db)
):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()

    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


# =========================
#  RECUPERAR CONTRASEÑA - PASO 1
# =========================
@router.post("/forgot-password")
def forgot_password(
    request: schemas.ForgotPasswordRequest,
    db: Session = Depends(database.get_db)
):
    user = db.query(models.User).filter(models.User.email == request.email).first()

    # Seguridad: no damos pistas
    if not user:
        return {"message": "Si el correo existe, se enviará un enlace de recuperación."}

    reset_token = auth.create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=15)
    )

    print("TOKEN DE RECUPERACIÓN:", reset_token)

    return {"message": "Se ha enviado un enlace de recuperación a tu correo (simulado)."}


# =========================
#  RECUPERAR CONTRASEÑA - PASO 2
# =========================
@router.post("/reset-password")
def reset_password(
    request: schemas.ResetPasswordRequest,
    db: Session = Depends(database.get_db)
):
    try:
        payload = auth.verify_token(request.token)
        username = payload.get("sub")
    except:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

    user = db.query(models.User).filter(models.User.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    hashed = auth.get_password_hash(request.new_password)
    user.hashed_password = hashed
    db.commit()

    return {"message": "Contraseña restablecida correctamente"}
