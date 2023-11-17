# Flask ML API: A Journey in Image Classification

## My Experience with the Project

**Welcome to my Flask ML API project!** As a passionate developer at Anyone AI, I was thrilled to tackle a fascinating challenge: automating the classification of a vast collection of images. This journey wasn't just about coding; it was about creating a tool that could streamline processes and enhance accuracy, a goal any tech enthusiast would be proud to pursue.

## The Challenge

In our digital world, images are everywhere, and categorizing them manually is a daunting task. My objective was clear: develop an automated solution to classify images into over 1000 categories using a Convolutional Neural Network (CNN) with TensorFlow. This solution had to be user-friendly, efficient, and robust, comprising a Web UI and a Python Flask API.

## The Solution

The heart of my project is the Web UI, where users can effortlessly upload an image and instantly receive its predicted category. The Python Flask API is the engine behind this - processing each image, feeding it into the CNN, and returning the classification as a JSON object. I prioritized error handling and user feedback, ensuring a seamless experience even when hiccups occur.

## The Learning Curve

Embarking on this project was also a learning journey for me. While we utilized a pre-trained TensorFlow CNN model, diving into its intricacies in the provided Jupyter notebook was an eye-opener and an immense motivation to deepen my understanding of these amazing models in the upcoming sprint.

## Technical Details

To bring this vision to life, I relied on a suite of powerful tools and technologies:

- Docker and docker-compose for a consistent development environment.
- VS Code, my IDE of choice, for a smooth coding experience.
- (Optional) Linux subsystem for Windows (WSL2) for enhanced performance.

## Installation and Setup

Getting started with the project is straightforward:

1. Clone the repository and navigate to the project directory.
2. Copy the `.env.original` file to `.env` and set the UID and GID environment variables (use `id -u` and `id -g` commands).
3. Use `docker-compose up --build -d` to launch the services.
4. To stop the services, run `docker-compose down`.

### Note on UID and GID in Docker

I've ensured security and portability by setting the UID (User ID) and GID (Group ID) in Docker. This approach avoids permission issues and guarantees that our containers run consistently across different systems.

## Code Style and Quality

In this project, code aesthetics and readability are paramount. I've adopted automated code formatting using Black and isort. This choice not only keeps our codebase clean but also streamlines contributions and code reviews.

## Testing: Ensuring Reliability

I've included unit tests to ensure the code's correctness and minimum requirements. These tests are crucial for maintaining the integrity of our solution. You can run them with ease using the provided commands in the `api/` and `model/` directories.

## The Future: Integration and End-to-End Testing

The project isn't just about individual components; it's about how they work together. End-to-end testing is the next big step, ensuring that our entire pipeline functions as intended. For more insights into our testing approach, refer to the `tests/` directory.

## Join Me on This Journey

This project isn't just code; it's a reflection of my passion and commitment to solving real-world problems with technology. I invite you to dive into the code, experiment with it, and join me on this exciting journey of innovation and learning. Let's explore the possibilities together!

