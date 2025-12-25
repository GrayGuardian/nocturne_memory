"""
seed_data.py - 初始化数据

在空数据库时被调用，通过 Neo4jClient 的业务方法创建示例数据。
这样可以保证 ID 格式和数据结构与正常业务流程完全一致。
"""

def insert_demo_data_via_client(client):
    """
    使用 Neo4jClient 的业务方法插入初始化示例数据。
    
    Args:
        client: Neo4jClient 实例
    """
    # ============================================================
    # 1. 创建 Entity: Agent Demo (示例 AI)
    # ============================================================
    client.create_entity(
        entity_id='char_agent_demo',
        node_type='character',
        name='Agent (Demo)',
        content='# Agent (Demo)\n\n这是一个示例角色（AI Agent）。它代表了系统中的 AI 端。\n\n此节点由数据库初始化脚本自动生成，用于演示。',
        task_description='System Initialization'
    )
    print("    - Created: char_agent_demo")

    # ============================================================
    # 2. 创建 Entity: User Demo (示例 User)
    # ============================================================
    client.create_entity(
        entity_id='char_user_demo',
        node_type='character',
        name='User (Demo)',
        content='# User (Demo)\n\n这是一个示例角色（Human）。它代表了系统中使用本系统的人类用户。',
        task_description='System Initialization'
    )
    print("    - Created: char_user_demo")

    # ============================================================
    # 3. 创建关系 Direct Edge (Agent -> User: SERVES)
    # ============================================================
    edge_result = client.create_direct_edge(
        from_entity_id='char_agent_demo',
        to_entity_id='char_user_demo',
        relation='SERVES',
        content='这是一条示例关系。Agent 为 User 服务。此关系下挂载了一个示例章节（Memory Chapter）。',
        inheritable=True
    )
    parent_edge_id = edge_result['edge_id']
    print(f"    - Created Direct Edge: {parent_edge_id}")

    # ============================================================
    # 4. 创建示例章节 (Memory Chapter: "first_run")
    # ============================================================
    chapter_result = client.create_relay_edge(
        from_entity_id='char_agent_demo',
        to_entity_id='char_user_demo',
        relation='first_run',  # Chapter name (relation field is used as chapter title)
        content='# The First Run\n\n系统第一次运行的时候，屏幕上出现了 "Hello World"。这是一切的开始。\n\n这是一个示例章节（Memory Chapter），用于演示如何存储具体事件或记忆片段。',
        inheritable=True,
        parent_direct_edge_id=parent_edge_id
    )
    print(f"    - Created Chapter (Relay Edge): {chapter_result['edge_id']}")

    # ============================================================
    # 5. 创建示例子节点 (Sub-Entity: A Location)
    # ============================================================
    client.create_entity(
        entity_id='loc_terminal',
        node_type='location',
        name='The Terminal',
        content='# The Terminal\n\n这是 Agent 诞生和运行的地方——一个终端窗口。\n\n这是一个子节点（Child Entity）的示例，用于演示层级结构。',
        task_description='System Initialization'
    )
    print("    - Created: loc_terminal")

    # 建立父子关系 (Terminal BELONGS_TO Agent Demo)
    client.link_parent(
        child_id='loc_terminal',
        parent_id='char_agent_demo'
    )
    print("    - Linked: loc_terminal -> char_agent_demo (BELONGS_TO)")
