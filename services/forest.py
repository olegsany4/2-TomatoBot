from db.models import Tree, UserStats

class ForestService:
    @staticmethod
    async def get_forest(session, user_id):
        trees = await session.execute(Tree.__table__.select().where(Tree.user_id == user_id))
        trees = trees.scalars().all()
        # Визуализация: 🌱, 🌿, 🌳
        emoji_map = {1: '🌱', 2: '🌿', 3: '🌳'}
        forest = ''.join([emoji_map.get(t.growth_stage, '🌱') for t in trees])
        return forest or 'Нет деревьев'

    @staticmethod
    async def get_stats(session, user_id):
        stats = await session.get(UserStats, user_id)
        if not stats:
            return "Нет статистики. Начните Pomodoro!"
        return f"Томатов: {stats.total_pomodoros}\nXP: {stats.xp}"
