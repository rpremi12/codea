import Head from 'next/head'
import Navbar from '/components/Navbar'
import styles from '../styles/Home.module.scss'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Codea</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <Navbar/>
      
      <main>
        <header>
          <h1>I want to get better at ______.</h1>
          <div className="concepts">
            <h2>Concepts</h2>
          </div>
          <div className="frameworks">
            <h2>Frameworks</h2>
          </div>
          <button>Search</button>
        </header>
      </main>
    </div>
  )
}
