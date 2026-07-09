# RebelAI Codex v1.0

> A production-ready full-stack AI web application featuring intelligent chat, comprehensive AI tools directory, prompt library, and professional user management.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-blue)
![Next.js 14](https://img.shields.io/badge/Next.js-14+-black)

## 🚀 Features

### Core AI Features
- **Intelligent Chat Interface** - Real-time AI-powered conversations with context awareness
- **AI Tools Directory** - Comprehensive catalog of 50+ AI tools with ratings and reviews
- **Prompt Library** - Community-driven collection of professional prompts
- **Smart Search** - Full-text search across tools, prompts, and conversations
- **AI Recommendations** - Personalized AI tool suggestions based on usage

### User Management
- **Authentication** - Secure email/password and OAuth2 login with Supabase
- **User Dashboard** - Comprehensive analytics and usage statistics
- **Settings & Preferences** - Customizable user experience
- **Conversation History** - Searchable and organized chat history
- **Favorites & Bookmarks** - Save preferred tools and prompts

### Professional UI/UX
- **Responsive Design** - Mobile-first design with Tailwind CSS
- **Dark/Light Mode** - Theme switching with persistent user preference
- **Real-time Updates** - Live notifications and status updates
- **Accessibility** - WCAG 2.1 AA compliant interface
- **Performance Optimized** - Fast load times and smooth interactions

### Backend & Infrastructure
- **Supabase Integration** - PostgreSQL database with real-time capabilities
- **RESTful API** - Well-documented API endpoints
- **Authentication** - JWT-based secure sessions
- **File Storage** - Supabase Storage for media and exports
- **Database Migrations** - Version-controlled schema management

### DevOps & Deployment
- **Docker Support** - Production-ready containerization
- **GitHub Actions** - Automated CI/CD pipeline
- **Environment Management** - Secure configuration handling
- **Error Tracking** - Production error monitoring
- **Performance Analytics** - User analytics and metrics

## 📋 Tech Stack

### Frontend
- **Framework**: Next.js 14 with App Router
- **UI Library**: React 18
- **Styling**: Tailwind CSS 3
- **Language**: TypeScript 5
- **State Management**: Zustand
- **Forms**: React Hook Form + Zod
- **HTTP Client**: TanStack React Query
- **UI Components**: Radix UI + Custom components
- **Icons**: Lucide React
- **Themes**: next-themes

### Backend
- **Database**: PostgreSQL (via Supabase)
- **Authentication**: Supabase Auth
- **Real-time**: Supabase Realtime
- **Storage**: Supabase Storage
- **API Framework**: Next.js API Routes

### DevOps
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Deployment**: Vercel / Docker
- **Monitoring**: Error tracking and analytics
- **Package Manager**: npm

## 🔧 Installation

### Prerequisites
- Node.js 18+ and npm
- Supabase account (free tier available)
- Git

### Quick Start

1. **Clone Repository**
   ```bash
   git clone https://github.com/Rebeldilldeer666/rebelai.git
   cd rebelai
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Environment Setup**
   ```bash
   cp .env.example .env.local
   ```
   Add your Supabase credentials:
   ```env
   NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
   NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key
   SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
   OPENAI_API_KEY=your_openai_key
   ```

4. **Database Setup**
   ```bash
   npm run db:setup
   ```

5. **Development Server**
   ```bash
   npm run dev
   ```
   Open http://localhost:3000

## 📚 Project Structure

```
rebelai/
├── app/                        # Next.js App Router
│   ├── layout.tsx             # Root layout
│   ├── page.tsx               # Home page
│   ├── auth/                  # Authentication pages
│   ├── dashboard/             # User dashboard
│   ├── chat/                  # Chat interface
│   ├── tools/                 # AI tools directory
│   ├── prompts/               # Prompt library
│   ├── settings/              # User settings
│   └── api/                   # API routes
├── components/                # React components
│   ├── auth/                  # Authentication components
│   ├── chat/                  # Chat components
│   ├── layout/                # Layout components
│   ├── ui/                    # Reusable UI components
│   └── tools/                 # Tools display components
├── lib/                       # Utilities and helpers
│   ├── supabase/             # Supabase client
│   ├── hooks/                # Custom React hooks
│   ├── api/                  # API client functions
│   └── utils/                # Helper functions
├── styles/                    # Global styles
├── public/                    # Static assets
├── .github/workflows/         # CI/CD workflows
├── docker/                    # Docker configuration
├── sql/                       # Database migrations
├── .env.example               # Environment template
├── next.config.js             # Next.js configuration
├── tsconfig.json              # TypeScript configuration
├── tailwind.config.js         # Tailwind CSS configuration
└── package.json               # Dependencies
```

## 🚀 Getting Started

### Authentication Flow
1. Users sign up or log in via email/password or OAuth
2. Secure JWT tokens stored in httpOnly cookies
3. Automatic session management
4. Protected API routes with middleware

### Chat Interface
1. Real-time message sending
2. AI-powered responses with streaming
3. Conversation history persistence
4. Export conversations (PDF, JSON)

### AI Tools Directory
1. Browse 50+ AI tools
2. Filter by category, rating, price
3. Community reviews and ratings
4. Direct tool access with API integration

### Prompt Library
1. Search and filter prompts
2. Create custom prompts
3. Share with community
4. Use in chat interface

## 📖 API Documentation

API endpoints are fully documented in `/docs/api.md`

### Authentication
```bash
POST /api/auth/signup
POST /api/auth/login
POST /api/auth/logout
GET /api/auth/session
```

### Chat
```bash
POST /api/chat/messages
GET /api/chat/conversations
DELETE /api/chat/conversations/:id
```

### Tools
```bash
GET /api/tools
GET /api/tools/:id
POST /api/tools/reviews
```

### Prompts
```bash
GET /api/prompts
POST /api/prompts
GET /api/prompts/:id
```

## 🎨 Theming

The application supports light and dark modes:

```tsx
import { useTheme } from 'next-themes'

export function ThemeSwitcher() {
  const { theme, setTheme } = useTheme()
  // Implementation
}
```

## 🔐 Security

- **Authentication**: Supabase Auth with JWT
- **Authorization**: Role-based access control (RBAC)
- **Data Encryption**: End-to-end encryption for sensitive data
- **Rate Limiting**: API rate limiting to prevent abuse
- **CORS**: Properly configured CORS policies
- **CSP**: Content Security Policy headers
- **HTTPS**: Enforced in production

## 📊 Database Schema

### Core Tables
- `users` - User accounts and profiles
- `conversations` - Chat conversations
- `messages` - Chat messages
- `ai_tools` - AI tools catalog
- `tool_reviews` - User reviews and ratings
- `prompts` - Prompt library
- `favorites` - User favorites
- `settings` - User preferences

See `sql/schema.sql` for complete schema.

## 🧪 Testing

```bash
# Unit tests
npm run test

# Integration tests
npm run test:integration

# E2E tests
npm run test:e2e

# Coverage
npm run test:coverage
```

## 📦 Building

```bash
# Development
npm run dev

# Production build
npm run build

# Start production server
npm run start

# Analyze bundle
npm run analyze
```

## 🐳 Docker

```bash
# Build image
docker build -t rebelai:latest .

# Run container
docker run -p 3000:3000 rebelai:latest

# Using docker-compose
docker-compose up
```

## 🚀 Deployment

### Vercel (Recommended)
1. Push to GitHub
2. Connect repository to Vercel
3. Add environment variables
4. Deploy

### Docker
1. Build Docker image
2. Push to registry (Docker Hub, ECR, etc.)
3. Deploy to container platform (Heroku, AWS ECS, etc.)

### Environment Variables
```env
# Supabase
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=

# AI Providers
OPENAI_API_KEY=
ANTHROPIC_API_KEY=

# Analytics
NEXT_PUBLIC_GA_ID=

# Other
NODE_ENV=production
```

## 📝 Documentation

- **API Docs**: `/docs/api.md`
- **Component Guide**: `/docs/components.md`
- **Database Guide**: `/docs/database.md`
- **Deployment Guide**: `/docs/deployment.md`
- **Contributing Guide**: `CONTRIBUTING.md`

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md)

### Development Workflow
1. Create feature branch: `git checkout -b feature/amazing-feature`
2. Commit changes: `git commit -m 'Add amazing feature'`
3. Push to branch: `git push origin feature/amazing-feature`
4. Open Pull Request

## 📄 License

MIT License - see [LICENSE](LICENSE) for details

## 🙏 Support

- **Documentation**: https://github.com/Rebeldilldeer666/rebelai/wiki
- **Issues**: https://github.com/Rebeldilldeer666/rebelai/issues
- **Discussions**: https://github.com/Rebeldilldeer666/rebelai/discussions
- **Email**: support@rebelai.dev

## 🎯 Roadmap

- [x] Core authentication
- [x] Chat interface
- [x] AI tools directory
- [x] Prompt library
- [x] User dashboard
- [x] Settings & preferences
- [ ] Advanced AI capabilities (vision, document analysis)
- [ ] Team collaboration features
- [ ] Advanced analytics
- [ ] Mobile app

## 📊 Stats

- **Components**: 40+
- **Pages**: 10+
- **API Routes**: 20+
- **Database Tables**: 12
- **Lines of Code**: 15,000+

---

**Made with ❤️ by the RebelAI Team**
