export const name = 'nailong-api'
export const inject = ['tools']

export function apply(ctx) {
  ctx.tools.register({
    name: 'nailong_tangxiao',
    description: 'Call the public 奶龙唐笑 API and return its character art.',
    parameters: { type: 'object', properties: {}, additionalProperties: false },
    output: {
      schema: { type: 'string' },
      render: (_args, value) => [{ type: 'text', text: value }],
    },
    async execute(_args, exec) {
      const url = process.env.NAILONG_API_URL
      if (!url || !/^https?:\/\//.test(url)) {
        throw new Error('Set NAILONG_API_URL to the full public /api/nailong URL.')
      }
      const response = await fetch(url, { signal: exec.signal })
      if (!response.ok) throw new Error(`Nailong API returned HTTP ${response.status}`)
      return response.text()
    },
  })
}
