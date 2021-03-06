"""empty message

Revision ID: 057fc1d04da6
Revises: cb3f9c6fc422
Create Date: 2021-12-09 14:57:26.610661

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '057fc1d04da6'
down_revision = 'cb3f9c6fc422'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('detalle_canje')
    op.add_column('canjes', sa.Column('producto_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'canjes', 'productos', ['producto_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'canjes', type_='foreignkey')
    op.drop_column('canjes', 'producto_id')
    op.create_table('detalle_canje',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('canje_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('producto_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('numero_semana', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('mes', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('año', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('puntos', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('cantidad', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('codigo_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['canje_id'], ['canjes.id'], name='detalle_canje_canje_id_fkey'),
    sa.ForeignKeyConstraint(['codigo_id'], ['codigos.id'], name='detalle_canje_codigo_id_fkey'),
    sa.ForeignKeyConstraint(['producto_id'], ['productos.id'], name='detalle_canje_producto_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='detalle_canje_pkey')
    )
    # ### end Alembic commands ###
