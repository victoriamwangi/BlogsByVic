"""empty message

Revision ID: f00c82ba0f3b
Revises: 87e5b9fafa6e
Create Date: 2022-05-15 19:38:34.096786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f00c82ba0f3b'
down_revision = '87e5b9fafa6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('commenter', sa.String(length=200), nullable=True),
    sa.Column('body', sa.String(length=100), nullable=False),
    sa.Column('timeposted', sa.DateTime(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['blog_id'], ['blogs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###