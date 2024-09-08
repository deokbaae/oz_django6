from tabom.models import Like


def do_like(user_id: int, article_id: int) -> Like:
    return Like.do_like(user_id, article_id)
