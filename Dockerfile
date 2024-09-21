# Step 1: Use a base image
FROM python:3.8-slim

# Step 2: Set the working directory in the container
WORKDIR /

# Step 3: Copy the project files into the container
COPY . /

# Step 4: Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Step 5: Expose a port if your project is a web service (optional)
#EXPOSE 5000

# Step 6: Set the default command to run your application
CMD ["streamlit", "run", "main.py"]
#streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"