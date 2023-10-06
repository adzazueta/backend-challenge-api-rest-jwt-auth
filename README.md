# Backend Developer Challenge: API Rest with JWT Authentication

Welcome to the challenge for the Backend Developer position! This README contains the challenge details and instructions for completing it.

## Project Description

The objective of this test is to evaluate your skills in designing and developing a secure and efficient RESTful API with JWT authentication. You'll need to implement three key endpoints and ensure that authentication works correctly:

1. **Login Endpoint**: This endpoint should receive user access data (e.g., username and password) and return a valid JWT token if the credentials are correct.

2. **Token Verification Endpoint**: This endpoint should receive a JWT token in the authorization header and verify if it's valid. It should return the decoded token information if it's correct.

3. **Protected Endpoint to Get GitHub Users**: This endpoint should be protected and only accessible with a valid JWT token in the authorization header. It should consume the public [GitHub API](https://docs.github.com/en/rest) to fetch a list of GitHub users and return it as a response.

You can use any technology or framework of your choice to complete this test. What we will primarily evaluate is the thinking and creativity in the implementation of the solution.

Happy Coding!!!