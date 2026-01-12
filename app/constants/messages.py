class ApiMessages:
    # Generic
    SUCCESS = "Operation successful"
    ERROR = "An error occurred"
    
    # Auth / Users
    LOGIN_SUCCESS = "Successfully logged in"
    LOGIN_FAILED = "Incorrect email or password"
    USER_NOT_FOUND = "User not found"
    USER_ALREADY_EXISTS = "User with this email already exists"    
    UNAUTHORIZED = "Authentication required"
    TOKEN_MISSING = "Missing or invalid Authorization header" 
    TOKEN_INVALID = "Invalid or expired token"

    # Exams
    EXAM_LOCKED = "This exam is currently locked"
    EXAM_NOT_FOUND = "Exam not found"
    EXAM_CREATED = "Exam created successfully"
    EXAM_UPDATED = "Exam updated successfully"
    EXAM_DELETED = "Exam deleted successfully"