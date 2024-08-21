from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Fast_API')


class Category(BaseModel):
    name: str


category = []


class Tag(BaseModel):
    name: str


tag = []


class Author(BaseModel):
    name: str
    surname: str
    profession: str
    age: int


author = []


class Post(BaseModel):
    title: str
    description: str


post = []


class Team(BaseModel):
    title: str
    description: str


team = []


@app.post('/category-create/')
async def category_create(cat: Category):
    category.append(cat)
    return {'message': 'Category create'}


@app.put('/category-update/')
async def update_category(category_id: int, cat: Category):
    category[category_id] = cat
    return {'message': cat}


@app.get('/category/')
async def category_retrieve():
    return {'category': category}


@app.patch('/category-update/{post_id}')
async def update_post(post_id: int, posts: Post):
    posts[post_id] = post
    return {'message': post}


@app.delete('/category-delete/')
async def category_delete(cat: Category):
    category.append(cat)
    return {'message', 'Category delete'}


@app.post('/tag-create/')
async def tag_create(tags: Tag):
    tag.append(tags)
    return {'message': 'Tag create'}


@app.put('/tag-update/')
async def update_tag(tag_id: int, tags: Tag):
    tag[tag_id] = tags
    return {'message': tags}


@app.get('/tag/')
async def tag_retrieve():
    return {'tags': tag}


@app.patch('/tag-update/{post_id}')
async def update_tag(tag_id: int, tags: Tag):
    tag[tag_id] = tags
    return {'message': tag}


@app.delete('/tag-delete/')
async def tag_delete(tags: Tag):
    tag.append(tags)
    return {'message', 'Tag delete'}
