"""add-api-key-auth-binding

Revision ID: 7b45942e39bb
Revises: 47cc7df8c4f3
Create Date: 2024-05-14 07:31:29.702766

"""
from alembic import op
import models as models
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7b45942e39bb'
down_revision = '47cc7df8c4f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_source_api_key_auth_bindings',
    sa.Column('id', models.StringUUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('tenant_id', models.StringUUID(), nullable=False),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('provider', sa.String(length=255), nullable=False),
    sa.Column('credentials', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.Column('disabled', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.PrimaryKeyConstraint('id', name='data_source_api_key_auth_binding_pkey')
    )
    with op.batch_alter_table('data_source_api_key_auth_bindings', schema=None) as batch_op:
        batch_op.create_index('data_source_api_key_auth_binding_provider_idx', ['provider'], unique=False)
        batch_op.create_index('data_source_api_key_auth_binding_tenant_id_idx', ['tenant_id'], unique=False)

    with op.batch_alter_table('data_source_bindings', schema=None) as batch_op:
        batch_op.drop_index('source_binding_tenant_id_idx')
        batch_op.drop_index('source_info_idx')

    op.rename_table('data_source_bindings', 'data_source_oauth_bindings')

    with op.batch_alter_table('data_source_oauth_bindings', schema=None) as batch_op:
        batch_op.create_index('source_binding_tenant_id_idx', ['tenant_id'], unique=False)
        batch_op.create_index('source_info_idx', ['source_info'], unique=False, postgresql_using='gin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table('data_source_oauth_bindings', schema=None) as batch_op:
        batch_op.drop_index('source_info_idx', postgresql_using='gin')
        batch_op.drop_index('source_binding_tenant_id_idx')

    op.rename_table('data_source_oauth_bindings', 'data_source_bindings')

    with op.batch_alter_table('data_source_bindings', schema=None) as batch_op:
        batch_op.create_index('source_info_idx', ['source_info'], unique=False)
        batch_op.create_index('source_binding_tenant_id_idx', ['tenant_id'], unique=False)

    with op.batch_alter_table('data_source_api_key_auth_bindings', schema=None) as batch_op:
        batch_op.drop_index('data_source_api_key_auth_binding_tenant_id_idx')
        batch_op.drop_index('data_source_api_key_auth_binding_provider_idx')

    op.drop_table('data_source_api_key_auth_bindings')
    # ### end Alembic commands ###
