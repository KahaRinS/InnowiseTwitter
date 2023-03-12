from DynamoDB.db import initialize_db


def add(page_id, subscribers, posts, likes):
    table = initialize_db().Table('Pages')

    # Добавляем новую запись
    # page_id = 'page1'
    # subscribers = 100
    # posts = 100
    # likes = 200
    table.put_item(
        Item={
            'page_id': page_id,
            'subscribers': subscribers,
            'posts': posts,
            'likes': likes
        }
    )

    # Получаем запись по ее идентификатору
    response = table.get_item(
        Key={
            'page_id': page_id
        }
    )
    item = response['Item']
    print(item)