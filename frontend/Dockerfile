FROM node:20.15

WORKDIR code

COPY package.json .
RUN npm install

COPY . .
CMD npm start


