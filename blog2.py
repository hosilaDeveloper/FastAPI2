from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Fast_API')


class Category(BaseModel):
    name: str


category = []


class Tag(BaseModel):
    name: str


tags = []


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


@app.post('/category-create/')
async def category_create(cat: Category):
    category.append(cat)
    return {'message': 'Category create'}


@app.put('/category-update/')
async def category_update(cat: Category):
    category.append(cat)
    return {'message:', 'Category update'}


@app.delete('/category-delete/')
async def category_delete(cat: Category):
    category.append(cat)
    return {'message', 'Category delete'}


@app.get('/category/')
async def retrieve_category():
    return {'category': category}


@app.post('/tag-create/')
async def tag_create(tag: Tag):
    tags.append(tag)
    return {'message': 'Tag create'}


@app.put('/tag-update/')
async def tag_update(tag: Tag):
    tags.append(tag)
    return {'message:', 'Tag update'}


@app.delete('/tag-delete/')
async def tag_delete(tag: Tag):
    tags.append(tag)
    return {'message', 'Tag delete'}


@app.get('/tags/')
async def retrieve_tags():
    return {'tag': tags}


@app.post('author-create')
async def author_create(aut: Author):
    author.append(aut)
    return {'message': 'Author create'}


@app.put('author-update')
async def author_update(aut: Author):
    author.append(aut)
    return {'message:', 'Author update'}


@app.delete('author-delete')
async def author_delete(aut: Author):
    author.append(aut)
    return {'message', 'Author delete'}


@app.get('/author/')
async def retrieve_author():
    return {'authors': author}


@app.post('post-create')
async def post_update(posts: Post):
    post.append(posts)
    return {'message': 'Post update'}


@app.put('post-update')
async def post_update(posts: Post):
    posts.append(post)
    return {'message:', 'Post update'}


@app.delete('post-delete')
async def post_delete(posts: Post):
    post.append(posts)
    return {'message', 'Post delete'}


@app.get('/post/')
async def retrieve_posts():
    return {'post': post}
