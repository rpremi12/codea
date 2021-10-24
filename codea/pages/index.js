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
        </header>
        <section className="bodycontent">  
        <div className="concepts">
            <h2>Concepts</h2>
            <button className="buttons">Front End</button>
            <button>Back End</button>
            <button>Machine Learning</button>
            <button>Cloud Computing</button>
          </div>
          <div className="frameworks">
            <h2>Frameworks</h2>
            <button>Python</button>
            <button>Django</button>
            <button>SQL</button>
            <button>React</button>
          </div>

          <button className="search w-100">Search</button>
          <hr/>
      </section>
      </main>
    </div>
  )
}
