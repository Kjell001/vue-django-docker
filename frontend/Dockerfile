FROM node:21-alpine as build-stage
WORKDIR /frontend
COPY package.json yarn.lock .yarnrc.yml ./
COPY .yarn ./.yarn
RUN yarn install
COPY . .
RUN yarn build

FROM nginx:1.25-alpine
COPY --from=build-stage /frontend/dist /frontend/dist
COPY nginx.conf /etc/nginx/conf.d/default.conf
