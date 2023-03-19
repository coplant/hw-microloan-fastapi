from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

from auth.models import User
from auth.manager import get_user_manager
from config import SECRET

# todo: set cookie security, same-site
cookie_transport = CookieTransport(cookie_name="session", cookie_max_age=3600, cookie_secure=False,
                                   cookie_samesite="none")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
