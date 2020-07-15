"""empty message

Revision ID: d20093efbf65
Revises: 1b921a26d402
Create Date: 2020-07-15 13:23:17.284782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd20093efbf65'
down_revision = '1b921a26d402'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cursos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('curso', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cursos_usuarios',
    sa.Column('usuarioID', sa.Integer(), nullable=True),
    sa.Column('cursoID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cursoID'], ['cursos.id'], ),
    sa.ForeignKeyConstraint(['usuarioID'], ['usuarios.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cursos_usuarios')
    op.drop_table('cursos')
    # ### end Alembic commands ###