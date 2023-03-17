from enum import Enum

from verification.models import Passport


async def get_unverified_users(items: list[Passport]):
    users = []
    for item in items:
        if not item.user.is_verified and item.filename:
            users.append(item)
    return users


async def is_unverified(item):
    return not item.is_verified and item.passport.filename
