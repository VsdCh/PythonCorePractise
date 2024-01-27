in file regular_expressions_validate_password:

^: Start character.
(?=.*[0-9]): Ensure string has at least a digit.
.{8,}: Ensure string has at least 8 characters.
$: End character.
