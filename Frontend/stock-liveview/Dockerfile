# Use the official Node.js image as the base image
FROM node:22

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Expose the port the app runs on
EXPOSE 3000

# Copy the source code to the container
COPY . .

# Set the environment variable
ENV MONGODB_URL="mongodb://host.docker.internal:27017,host.docker.internal:27018,host.docker.internal:27019/stocks?replicaSet=rs0"

# Start the server when the container starts
CMD ["node", "app.js"]
