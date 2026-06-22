admin_permissions={"read","write","execute","delete"}
editor_permissions={"read","write"}

required_permission="delete"

if required_permission in editor_permissions:
    print("Editor can perform the required action.")
else:
    print("Editor does not have the required permission.")
