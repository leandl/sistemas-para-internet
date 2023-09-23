export class GithubApiServiceError extends Error {
  constructor(message: string) {
    super();
    this.name = "GithubApiServiceError";
    this.message = message;
  }
}
