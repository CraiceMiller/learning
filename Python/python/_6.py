def get_user_access_level(is_active: bool, 
                        role: str,
                        subscription_tier: str) -> str:
    """
    Determines a user's access level based on activity, role, and subscription.

    Args:
        is_active (bool): True if the user account is active, False otherwise.
        role (str): The user's role (e.g., "admin", "member", "guest", "viewer").
        subscription_tier (str): The user's subscription tier (e.g., "premium", "standard", "basic", "none").

    Returns:
        str: A string describing the user's access level.

    My conclusion:
        None
    """


    #this will return if the user is not active
    if not is_active:
        return "No Access (Inactive Account)"
    
    #returning base on the role 
    if role == "admin":
        return "Full Admin Access"
    
    if role == "guest":
        return  "Limited Guest Access" 
    
    if role == "viewer":
        return  "View Only Access"
    
    #returning members
    if role !="member":
        return "No Access (Invalid Role)"
    
    if subscription_tier == "premium":
        return "Premium Member Access"
    
    if subscription_tier == "standard":
        return "Standard Member Access"


    return "Basic Member Access"

def can_process_transaction(is_account_active: bool,
                            is_fraud_detected: bool,
                            transaction_amount: float,
                            customer_segment: str) -> bool:
    """
    Checks if a transaction can be processed based on various conditions.

    Args:
        is_account_active (bool): True if the account is active.
        is_fraud_detected (bool): True if fraud is detected for this transaction.
        transaction_amount (float): The amount of the transaction.
        customer_segment (str): The customer's segment (e.g., "premium", "standard", "guest").

    Returns:
        bool: True if the transaction can be processed, False otherwise.
    """
    if not is_account_active:
        print("Cannot process transaction: account is not active.")
        return False 
    
    if  is_fraud_detected: 
        print("Cannot process transaction: fraud detected.")
        return False
    

    if transaction_amount < 0:
        print("Cannot process transaction: amount must be positive.")
        return False 
    
    if customer_segment == "guest": 
        print("Cannot process transaction: customer is a guest.")
        return False 
    
    # All conditions met, transaction can be processed   
    return True 


def is_document_valid(document_content: str | None,
                      file_type: str,
                      min_length: int,
                      max_length: int) -> bool:
    """
    Checks if a document is valid based on its content, type, and length.

    Args:
        document_content (str | None): The content of the document, or None if missing.
        file_type (str): The type of the file (e.g., "pdf", "docx", "txt").
        min_length (int): The minimum required length of the content.
        max_length (int): The maximum allowed length of the content.

    Returns:
        bool: True if the document is valid, False otherwise.
    """
    if document_content is None:
        print("Document invalid: content is missing (None).")
        return False  
    
    if len(document_content) < 1:
        print("Document invalid: content is empty.")
        return False
    
   
    if len(document_content) < min_length: 
        print("Too short")
        return False

    if len(document_content) > max_length:
        print("Too long")
        return False

    

    
    if file_type not in  ("pdf" , "docx",  "txt"):
        print(f"Document invalid: unsupported file type '{file_type}'.")
        return False
    
    return True 
    


    




# --- Test Cases ---
print(f"Test 1: {is_document_valid('Hello World', 'pdf', 5, 20)}") # Expected: True
print(f"Test 2: {is_document_valid(None, 'pdf', 5, 20)}")          # Expected: False (Content is None)
print(f"Test 3: {is_document_valid('', 'pdf', 5, 20)}")            # Expected: False (Content is empty string)
print(f"Test 4: {is_document_valid('Hi', 'pdf', 5, 20)}")           # Expected: False (Too short)
print(f"Test 5: {is_document_valid('This is a very long document content.', 'pdf', 5, 20)}") # Expected: False (Too long)
print(f"Test 6: {is_document_valid('Valid content', 'jpg', 5, 20)}") # Expected: False (Unsupported file type)


# --- Test Cases ---
print(f"Test 1: {can_process_transaction(True, False, 100.0, 'standard')}") # Expected: True
print(f"Test 2: {can_process_transaction(False, False, 50.0, 'premium')}")  # Expected: False (Inactive account)
print(f"Test 3: {can_process_transaction(True, True, 200.0, 'standard')}")   # Expected: False (Fraud detected)
print(f"Test 4: {can_process_transaction(True, False, -10.0, 'premium')}")  # Expected: False (Negative amount)
print(f"Test 5: {can_process_transaction(True, False, 75.0, 'guest')}")     # Expected: False (Guest customer)


# --- Test Cases (Use these to verify your optimized function) ---
print(f"Test 1 (Active Admin): {get_user_access_level(True, 'admin', 'any')}")
# Expected: Full Admin Access

print(f"Test 2 (Active Premium Member): {get_user_access_level(True, 'member', 'premium')}")
# Expected: Premium Member Access

print(f"Test 3 (Active Standard Member): {get_user_access_level(True, 'member', 'standard')}")
# Expected: Standard Member Access

print(f"Test 4 (Active Basic Member): {get_user_access_level(True, 'member', 'basic')}")
# Expected: Basic Member Access

print(f"Test 5 (Active Guest): {get_user_access_level(True, 'guest', 'none')}")
# Expected: Limited Guest Access

print(f"Test 6 (Active Viewer): {get_user_access_level(True, 'viewer', 'none')}")
# Expected: View Only Access

print(f"Test 7 (Active Invalid Role): {get_user_access_level(True, 'unregistered', 'none')}")
# Expected: No Access (Invalid Role)

print(f"Test 8 (Inactive Account): {get_user_access_level(False, 'admin', 'premium')}")
# Expected: No Access (Inactive Account)"""