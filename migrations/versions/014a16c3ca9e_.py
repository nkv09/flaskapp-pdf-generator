"""empty message

Revision ID: 014a16c3ca9e
Revises: 47f93ae0a38d
Create Date: 2020-05-10 00:43:10.655802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '014a16c3ca9e'
down_revision = '47f93ae0a38d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('videos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_videos_title'), 'videos', ['title'], unique=False)
    op.create_table('question_video',
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('video_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['catalog_questions.id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['videos.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question_video')
    op.drop_index(op.f('ix_videos_title'), table_name='videos')
    op.drop_table('videos')
    # ### end Alembic commands ###
