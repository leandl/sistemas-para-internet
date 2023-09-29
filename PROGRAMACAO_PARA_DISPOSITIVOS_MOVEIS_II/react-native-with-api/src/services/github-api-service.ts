import { GithubApiServiceError } from "../utils/errors/github-api-service-error";
import { HttpCode } from "../utils/http-code";

export type UserGithub = {
  login: string;
  avatar_url: string;
  name: string;
} & Record<string, any>;

export type RepositoryGithub = {
  name: string;
  description: string | null;
  language: string;
} & Record<string, any>;

export class GithubApiService {
  static async getUserInformation(username: string): Promise<UserGithub> {
    const response = await fetch(`https://api.github.com/users/${username}`);

    if (response.status === HttpCode.NOT_FOUND) {
      throw new GithubApiServiceError("Usuário não Encontrado!");
    }

    if (response.status !== HttpCode.OK) {
      throw new GithubApiServiceError("Erro Desconhecido!");
    }

    const user = await response.json();
    return user;
  }

  static async getReposByUsername(
    username: string
  ): Promise<RepositoryGithub[]> {
    const response = await fetch(
      `https://api.github.com/users/${username}/repos`
    );

    if (response.status === HttpCode.NOT_FOUND) {
      throw new GithubApiServiceError("Repositório não Encontrado!");
    }

    if (response.status !== HttpCode.OK) {
      throw new GithubApiServiceError("Erro Desconhecido!");
    }

    const data = await response.json();
    return data;
  }
}
