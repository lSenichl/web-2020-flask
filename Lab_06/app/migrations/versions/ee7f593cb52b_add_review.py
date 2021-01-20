"""Add Review

Revision ID: ee7f593cb52b
Revises: cafed63d7219
Create Date: 2021-01-17 16:59:51.003407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee7f593cb52b'
down_revision = 'cafed63d7219'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lab6_reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['lab6_courses.id'], name=op.f('fk_lab6_reviews_course_id_lab6_courses')),
    sa.ForeignKeyConstraint(['user_id'], ['lab6_users.id'], name=op.f('fk_lab6_reviews_user_id_lab6_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_lab6_reviews'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lab6_reviews')
    # ### end Alembic commands ###