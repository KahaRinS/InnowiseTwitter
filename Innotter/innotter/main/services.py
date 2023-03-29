class LikeService:
    def add_like(obj, user):
        obj.likes.add(user)
        return obj

    def remove_like(obj, user):
        obj.likes.remove(user)
        return obj


class FollowService:
    def add_follow(self, obj, user):
        if obj.is_private:
            obj.follow_requests.add(user)
        else:
            obj.followers.add(user)
        return obj

    def delete_follow(self, obj, user):
        if user in obj.follow_requests.all():
            obj.follow_requests.remove(user)
        if user in obj.followers.all():
            obj.followers.remove(user)
        return obj
