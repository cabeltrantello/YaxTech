# --- Build Stage ---
# Use a Node.js image to build the React application
FROM node:18-alpine AS build

WORKDIR /app

# Copy package files and install dependencies
# This leverages Docker's layer caching
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application source code
COPY . .

# Build the application for production
# This will create a 'dist' folder with static assets
RUN npm run build

# --- Serve Stage ---
# Use a lightweight Nginx image to serve the static files
FROM nginx:1.25-alpine

# Copy the built static files from the 'build' stage
COPY --from=build /app/dist /usr/share/nginx/html

# Copy the Nginx configuration to handle SPA routing
# This is not strictly needed with our reverse proxy, but good practice
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# The default Nginx command will start the server
CMD ["nginx", "-g", "daemon off;"]
