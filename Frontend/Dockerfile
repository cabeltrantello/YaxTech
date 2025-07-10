# --- Build Stage ---
FROM node:18-alpine AS build
WORKDIR /app

# Copy dependency files from the root context first to leverage Docker cache
COPY package.json package-lock.json ./
RUN npm install

# Copy only the necessary frontend source code and config files
COPY ./Frontend/src ./src
COPY ./Frontend/public ./public
COPY ./Frontend/index.html ./
COPY ./Frontend/tailwind.config.js ./
COPY ./Frontend/vite.config.js ./
COPY ./Frontend/postcss.config.js ./

# Build the application for production
RUN npm run build

# --- Serve Stage ---
FROM nginx:1.25-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

