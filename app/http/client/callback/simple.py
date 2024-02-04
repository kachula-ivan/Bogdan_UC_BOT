from aiogram import Router

from app.filters.isActive import IsActive

router = Router()
router.message.filter(IsActive())

