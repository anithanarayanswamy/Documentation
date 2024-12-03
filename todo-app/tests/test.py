# tests/test_todo.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TodoModel:
    """ Todo Model """
    def __init__(self):
        self.driver = None
    
    def start_application(self):
        """v_start vertex"""
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost:5000")
        print("Application started")
    
    def verify_empty_state(self):
        """v_empty vertex"""
        todo_items = self.driver.find_elements(By.CLASS_NAME, "todo-item")
        assert len(todo_items) == 0
        print("Verified empty state")
    
    def verify_list_state(self):
        """v_list vertex"""
        todo_items = self.driver.find_elements(By.CLASS_NAME, "todo-item")
        assert len(todo_items) > 0
        print("Verified list state")
    
    def initialize(self):
        """Edge from start to empty"""
        print("Initializing application")
        pass
    
    def add_todo(self):
        """Edge for adding todos"""
        input_field = self.driver.find_element(By.NAME, "todo")
        input_field.send_keys(f"Test Todo {time.time()}")
        input_field.send_keys(Keys.RETURN)
        time.sleep(1)
        print("Added todo item")
    
    def toggle_todo(self):
        """Edge for toggling todo state"""
        todo_link = self.driver.find_element(By.CLASS_NAME, "todo-item").find_element(By.TAG_NAME, "a")
        todo_link.click()
        time.sleep(1)
        print("Toggled todo item")
    
    def delete_todo(self):
        """Edge for deleting todo"""
        delete_button = self.driver.find_element(By.CLASS_NAME, "delete-btn")
        delete_button.click()
        time.sleep(1)
        print("Deleted todo item")

    def cleanup(self):
        """Cleanup after tests"""
        if self.driver:
            self.driver.quit()
            print("Cleaned up resources")