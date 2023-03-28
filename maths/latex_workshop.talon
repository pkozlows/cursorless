title: /\.tex/
-
tag(): user.maths

#for manipulating second quantization

create <user.key_or_letter>:
    insert("a")
    user.maths_superscript("\\dagger")
    user.maths_subscript(key_or_letter)

destroy <user.key_or_letter>:
    insert("a")
    user.maths_subscript(key_or_letter)
    
ket:
    insert("\\ket{{}}")

bra:
    insert("\\bra{{}}") 

plain ket:
    insert("\\ket{{0}}")

plain bra:
    insert("\\bra{{0}}")

face factor:
    user.insert_between("(", ")")
    insert("-1")
    key(right)
    user.maths_begin_superscript()

# by commend [<user.any_alphanumeric_key>] that:
#     insert(any_alphanumeric_key or "that")

# kronecker [<user.kron_choices>] <user.any_alphanumeric_key> <user.any_alphanumeric_key>:
#     insert("\\delta")
#     user.maths_begin_subscript()
#     (insert(kron_choices)
#     insert(any_alphanumeric_key_1)
#     key(right))
#     # or
#     (
#     insert(any_alphanumeric_key_1)
#     )
#     #then do
#     (
#     insert(kron_choices)
#     insert(any_alphanumeric_key_2)
#     key(right)
#     )
#     #or
#     (
#     insert(any_alphanumeric_key_2)
#     )
#     user.maths_end_subscript()